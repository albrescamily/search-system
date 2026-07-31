import { API_BASE_URL } from "./apiConfig";

export const fetchImages = async () => {
  const response = await fetch(`${API_BASE_URL}/images`);

  if (!response.ok) {
    throw new Error(`Failed to fetch images: ${response.statusText}`);
  }

  const data = await response.json();
  return data.images;
};


export const deleteImage = async (key) => {
  const response = await fetch(
    `${API_BASE_URL}/delete-image?key=${encodeURIComponent(key)}`,
    { method: "DELETE" }
  );

  if (!response.ok) {
    throw new Error(`Failed to delete ${key}: ${response.statusText}`);
  }

  return response.json();
};


