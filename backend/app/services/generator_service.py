from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from sqlalchemy.orm import Session
from ..helpers.api_client import fetch_realtime_data
from .. import models
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_campaign(product_id: int, db: Session) -> str:
    """Generate a marketing campaign."""
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
        Create three unique ad copies for a marketing campaign.

        Product: {product_name}
        Description: {product_description}

        Audience Insights:
        {audience_data}

        Competitor Insights:
        {competitor_data}
        """
    )
    formatted_prompt = prompt_template.format(
        product_name=product.product_name,
        product_description=product.product_description,
        audience_data=audience_data,
        competitor_data=competitor_data
    )

    # Use ChatOpenAI for chat models with API key
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        openai_api_key=OPENAI_API_KEY  # Pass the API key explicitly
    )

    try:
        # Use the rendered prompt with ChatOpenAI
        messages = [
            SystemMessage(content="You are a creative assistant for marketers."),
            HumanMessage(content=formatted_prompt)
        ]
        response = llm(messages)
        return response.content
    except Exception as e:
        logger.error(f"Failed to generate campaign content: {e}")
        raise ValueError("Error generating campaign content")