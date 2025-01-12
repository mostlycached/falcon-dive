import React, { useState } from "react";

function InputPage() {
  const [formData, setFormData] = useState({
    productName: "",
    productDescription: "",
    targetAudience: "",
    brandTone: "Friendly",
    competitors: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  return (
    <div className="max-w-lg mx-auto mt-10 p-5 border border-gray-300 rounded-lg">
      <h1 className="text-2xl font-bold mb-5">Set Up Your Campaign</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="productName" className="block font-medium text-gray-700">
            Product Name
          </label>
          <input
            type="text"
            id="productName"
            name="productName"
            value={formData.productName}
            onChange={handleChange}
            placeholder="Enter your product name"
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div>
          <label htmlFor="productDescription" className="block font-medium text-gray-700">
            Product Description
          </label>
          <textarea
            id="productDescription"
            name="productDescription"
            value={formData.productDescription}
            onChange={handleChange}
            placeholder="Describe your product"
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div>
          <label htmlFor="targetAudience" className="block font-medium text-gray-700">
            Target Audience
          </label>
          <input
            type="text"
            id="targetAudience"
            name="targetAudience"
            value={formData.targetAudience}
            onChange={handleChange}
            placeholder="e.g., Millennials, Gen Z"
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
        <div>
          <label htmlFor="brandTone" className="block font-medium text-gray-700">
            Brand Tone
          </label>
          <select
            id="brandTone"
            name="brandTone"
            value={formData.brandTone}
            onChange={handleChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          >
            <option value="Friendly">Friendly</option>
            <option value="Luxury">Luxury</option>
            <option value="Playful">Playful</option>
            <option value="Professional">Professional</option>
          </select>
        </div>
        <div>
          <label htmlFor="competitors" className="block font-medium text-gray-700">
            Competitors
          </label>
          <input
            type="text"
            id="competitors"
            name="competitors"
            value={formData.competitors}
            onChange={handleChange}
            placeholder="List competitors (comma-separated)"
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
        >
          Generate Insights
        </button>
      </form>
    </div>
  );
}

export default InputPage;
