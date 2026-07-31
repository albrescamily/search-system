import { API_BASE_URL } from "./apiConfig";

export const triggerFileDialog = (inputRef) => {
  inputRef.current?.click();
};

export const getUploadedFiles = (event) => {
  return Array.from(event.target.files || []);
};

export const handleUploadedFiles = (event, callback) => {
  const files = getUploadedFiles(event);

  if (!files.length) return;

  callback(files);
};

export const uploadFilesToS3 = async (files) => {
  const uploads = files.map(async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(`${API_BASE_URL}/upload`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Failed to upload ${file.name}: ${response.statusText}`);
    }

    return response.json();
  });

  return Promise.all(uploads);
};

