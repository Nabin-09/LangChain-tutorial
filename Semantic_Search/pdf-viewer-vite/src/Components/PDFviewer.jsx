import React, { useState } from "react";

function App() {
  const [pdfData, setPdfData] = useState(null);

  const handleFetchData = async () => {
    const response = await fetch("http://localhost:8000/pdfdata");
    const data = await response.json();
    setPdfData(data);
  };

  return (
    <div>
      <button onClick={handleFetchData}>Show First Page PDF Data</button>
      {pdfData && (
        <div>
          <h2>Page Content</h2>
          <p>{pdfData.page_content}</p>
          <h4>Metadata</h4>
          <pre>{JSON.stringify(pdfData.metadata, null, 2)}</pre>
          <p>Total pages: {pdfData.total_pages}</p>
        </div>
      )}
    </div>
  );
}

export default App;
