from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from sqlalchemy.orm import Session
from ..helpers.api_client import fetch_realtime_data
from .. import models
import os, json

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_campaign(product_id: int, db: Session, use_dummy: bool = False) -> dict:
    """Generate a marketing campaign or return dummy data."""
    if use_dummy:
        return {
            "recommendations": [
                {
                    "type": "text",
                    "content": "Ad Copy 1: Make every sip count with our eco-friendly bottle.",
                    "title": "Eco Ad #1",
                    "tags": ["Eco-friendly", "Sustainability"]
                },
                {
                    "type": "deck",
                    "content": ["Slide 1: Eco-friendly", "Slide 2: Benefits", "Slide 3: Call to Action"],
                    "title": "Deck Presentation",
                    "tags": ["Interactive", "Visual"]
                },
                {
                    "type": "video",
                    "content": {
                        "component": "VideoComponentName",
                        "durationInFrames": 150,
                        "fps": 30
                    },
                    "title": "Promotional Video",
                    "tags": ["Dynamic", "Visual"]
                }
            ]
        }

    # Fetch product data
    product = db.query(models.InputData).filter(models.InputData.id == product_id).first()
    if not product:
        raise ValueError("Product not found")

    # Fetch real-time data
    audience_data = fetch_realtime_data(f"{product.target_audience} news", "audience")
    competitor_data = fetch_realtime_data(f"{product.competitors} market news", "competitor")

    # Create and format the prompt
    prompt_template = PromptTemplate(
        input_variables=["product_name", "product_description", "audience_data", "competitor_data"],
        template="""
        Generate three unique marketing recommendations in JSON format:
        [
            {{
                "type": "text",
                "content": "Your text ad copy here",
                "title": "Ad title here",
                "tags": ["tag1", "tag2"]
            }},
            {{
                "type": "deck",
                "content": ["Slide 1 content", "Slide 2 content", "Slide 3 content"],
                "title": "Deck title here",
                "tags": ["tag1", "tag2"]
            }},
            {{
                "type": "video",
                "content": {{
                    "component": "VideoComponentName",
                    "durationInFrames": 150,
                    "fps": 30
                }},
                "title": "Video title here",
                "tags": ["tag1", "tag2"]
            }}
        ]
        Product: {product_name}
        Description: {product_description}
        Audience Insights: {audience_data}
        Competitor Insights: {competitor_data}
        """
    )
    formatted_prompt = prompt_template.format(
        product_name=product.product_name,
        product_description=product.product_description,
        audience_data=audience_data,
        competitor_data=competitor_data
    )

    # Call the LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        openai_api_key=OPENAI_API_KEY
    )

    try:
        messages = [
            SystemMessage(content="You are a creative assistant for marketers."),
            HumanMessage(content=formatted_prompt)
        ]
        response = llm.invoke(messages)

        # Clean the LLM response content
        cleaned_content = clean_response_content(response.content)
        
        # Parse the cleaned content as JSON
        return json.loads(cleaned_content)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse LLM response: {e}")
        raise ValueError("LLM response is not valid JSON")
    except Exception as e:
        logger.error(f"Failed to generate campaign content: {e}")
        raise ValueError("Error generating campaign content")
    

def clean_response_content(response_content: str) -> str:
    """Clean the LLM response content to ensure it's valid JSON."""
    # Strip leading and trailing whitespace
    response_content = response_content.strip()
    
    # Remove markdown code block syntax if present
    if response_content.startswith("```json"):
        response_content = response_content[7:]  # Remove "```json"
    if response_content.endswith("```"):
        response_content = response_content[:-3]  # Remove "```"
    
    return response_content