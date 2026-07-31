import { useRef } from "react";
import {
  triggerFileDialog,
  handleUploadedFiles,
  uploadFilesToS3,
} from "../../utils/uploadUtils";
import "./Header.css"

export default function Header() {
  const fileInputRef = useRef(null);

  return (
    <header className="header">
      <h1>Gallery</h1>

      <input
        className="search"
        type="search"
        placeholder="Search images..."
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