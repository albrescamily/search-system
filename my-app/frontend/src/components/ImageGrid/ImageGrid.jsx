import { useEffect } from "react";
import { fetchImages, deleteImage } from "../../utils/imageUtils";
import "./ImageGrid.css";

export default function ImageGrid({ images, setImages }) {
  useEffect(() => {
    fetchImages()
      .then((fetched) => setImages(fetched))
      .catch((err) => console.error("Failed to load images:", err));
  }, []);

const handleDelete = async (key) => {
    try {
      await deleteImage(key);
      setImages((prev) => prev.filter((image) => image.key !== key));
    } catch (err) {
      console.error("Failed to delete image:", err);
    }
  };

  return (
    <section className="image-grid">
      {images.map((image) => (
        <div key={image.key} className="image-card">
          <img src={image.url} alt={image.key} />
          <div className="image-card__title">{image.key}</div>
          <button
            type="button"
            className="image-card__delete"
            onClick={() => handleDelete(image.key)}
          >
            Delete
          </button>
        </div>
      ))}
    </section>
  );
}