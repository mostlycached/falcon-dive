import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom'; // Import useParams
import RecommendationCard from '../components/RecommendationCard';

const RecommendationPage = () => {
  const { productId } = useParams();
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRecommendations = async () => {
      setLoading(true);
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/generate?product_id=${productId}&use_dummy=true`);
        const data = await response.json();
        if (response.ok) {
          setRecommendations(data.recommendations.recommendations);
        } else {
          setError(data.detail || 'Failed to fetch recommendations.');
        }
      } catch (err) {
        setError('An error occurred while fetching recommendations.');
      } finally {
        setLoading(false);
      }
    };

    fetchRecommendations();
  }, [productId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Generated Recommendations</h1>
      <div className="grid gap-4">
        {recommendations.map((rec, index) => (
          <RecommendationCard key={index} recommendation={rec} />
        ))}
      </div>
    </div>
  );
};

export default RecommendationPage;