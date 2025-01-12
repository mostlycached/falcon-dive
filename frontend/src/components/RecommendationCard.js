import React from 'react';
import PropTypes from 'prop-types';

const RecommendationCard = ({ recommendation }) => {
  const { type, title, content, tags } = recommendation;

  const renderContent = () => {
    if (type === 'text') {
      return <p>{content}</p>;
    }

    if (type === 'deck') {
      return (
        <ul className="list-disc ml-4">
          {content.map((slide, index) => (
            <li key={index}>{slide}</li>
          ))}
        </ul>
      );
    }

    if (type === 'video') {
      return (
        <div>
          <p>Component: {content.component}</p>
          <p>Duration: {content.durationInFrames} frames</p>
          <p>FPS: {content.fps}</p>
        </div>
      );
    }

    return <p>Unsupported content type</p>;
  };

  return (
    <div className="border border-gray-300 rounded-lg p-4 shadow-sm space-y-3">
      <h2 className="text-lg font-semibold">{title || 'Untitled Recommendation'}</h2>
      <div className="text-sm text-gray-500 space-x-2">
        {tags?.map((tag, index) => (
          <span key={index} className="inline-block bg-gray-100 rounded px-2 py-1">
            #{tag}
          </span>
        ))}
      </div>
      <div className="mt-2">{renderContent()}</div>
    </div>
  );
};

RecommendationCard.propTypes = {
  recommendation: PropTypes.shape({
    type: PropTypes.oneOf(['text', 'deck', 'video']).isRequired,
    title: PropTypes.string,
    content: PropTypes.any.isRequired,
    tags: PropTypes.arrayOf(PropTypes.string),
  }).isRequired,
};

export default RecommendationCard;