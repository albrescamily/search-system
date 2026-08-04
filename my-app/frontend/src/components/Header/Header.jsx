import { useRef, useState } from "react";
import {
  triggerFileDialog,
  handleUploadedFiles,
  uploadFilesToS3,
} from "../../utils/uploadUtils";
import { sendQuery } from "../../utils/searchUtils";
import "./Header.css"

export default function Header({ setImages }) {
  const fileInputRef = useRef(null);
  const [query, setQuery] = useState("");

  const handleSendQuery = async () => {
    if (!query.trim()) return;

    try {
      const images = await sendQuery(query);
      setImages(images);
    } catch (err) {
      console.error("Search failed:", err);
    }
  };

  return (
    <header className="header">
      <h1>Gallery</h1>

      <input
        className="search"
        type="search"
        placeholder="Search images..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") handleSendQuery();
        }}
      />

      <button
        type="button"
        className="upload"
        onClick={() => triggerFileDialog(fileInputRef)}
      >
        ↑ Upload
      </button>

      <input
        ref={fileInputRef}
        type="file"
        accept="image/*"
        multiple
        hidden
        onChange={(e) =>
          handleUploadedFiles(e, async (files) => {
            try {
              await uploadFilesToS3(files);
            } catch (err) {
              console.error("Upload failed:", err);
            }
          })
        }
      />
    </header>
  );
}