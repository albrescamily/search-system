import { API_BASE_URL } from "./apiConfig";

export const sendQuery = async (query) => {
  const response = await fetch(
    `${API_BASE_URL}/query_text?query=${encodeURIComponent(query)}`,
    { method: "POST" }
  );

  if (!response.ok) {
    throw new Error(`Failed to send query: ${response.statusText}`);
  }

  const data = await response.json();
  return data.images;
};
