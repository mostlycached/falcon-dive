import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import InputPage from "./pages/InputPage";
import RecommendationPage from './pages/RecommendationPage';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <Routes>
          <Route path="/" element={<InputPage />} />
          <Route path="/recommendations/:productId" element={<RecommendationPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
