import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import "src/pages/AssetsList.css";
import useHttpGet from "src/lib/hooks/useHttpGet";

const AssetsList = () => {
  const [assets, setAssets] = useState([]);
  const httpGet = useHttpGet();

  const getAssets = async () => {
    const resp = await httpGet("http://localhost:8000/api/get-assets-list");

    if (resp.code === 200) {
      setAssets(resp.data);
    } else {
      console.error("Error fetching assets:", resp.error);
    }
  };

  useEffect(() => {
    getAssets();
  }, []);

  return (
    <div className="container">
      <button className="backBtn" onClick={() => window.history.go(-1)}>
        <span className="arrow">«</span> Go Back
      </button>
      <h1>Asset List</h1>
      <div className="details_section">
        {assets.map((asset) => (
          <div key={asset.id} className="detail_card">
            <Link to={`/assets/${asset.id}`}>
              <p className="label">{asset.name}</p>
            </Link>
            <p className="value">{asset.category}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AssetsList;
