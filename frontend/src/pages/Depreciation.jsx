import { useState } from "react";
import { toast } from "react-toastify";
import { Link } from "react-router-dom";

import "src/pages/Depreciation.css";
import Button from "src/lib/components/Button";
import FormField from "src/lib/components/FormField";
import useHttpPost from "src/lib/hooks/useHttpPost";
import DepreciationDetails from "src/pages/components/DepreciationDetails";

const Depreciation = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [isDisable, setIsDisable] = useState(false);
  const [assetDetails, setAssetDetails] = useState({
    assetName: "",
    purchaseCost: "",
    purchaseDate: "",
    category: "",
    totalUnitsOfProduction: "",
  });
  const [depreciationDetails, setDepreciationDetails] = useState();

  const httpPost = useHttpPost();

  const handleChange = (name, value) => {
    setIsDisable(false);
    setDepreciationDetails(null);
    setAssetDetails({
      ...assetDetails,
      [name]: value,
    });
  };

  const getDepreciationDetails = async (e) => {
    e.preventDefault();

    // Validate form values.
    if (
      assetDetails.assetName.trim() === "" ||
      assetDetails.category.trim() === ""
    ) {
      toast.error("Please enter valid asset name and category.");
      return;
    }

    setIsLoading(true);
    setIsDisable(true);
    const resp = await httpPost("http://localhost:8000/api/find-depreciation", {
      name: assetDetails.assetName,
      purchase_cost: assetDetails.purchaseCost,
      purchase_date: assetDetails.purchaseDate,
      category: assetDetails.category,
      total_units_of_production: assetDetails.totalUnitsOfProduction || 0,
    });
    setIsLoading(false);
    if (resp.code === 200) {
      setDepreciationDetails(resp.data);
      toast.success("Added successfully.");
    } else {
      toast.error(
        "We are facing some issues right now. Please try again later."
      );
    }
  };

  return (
    <div className="mainDiv">
      <Link to="/assets" className="listLink">List of previous added asset</Link>
      <h1>Asset Form</h1>
      <form onSubmit={getDepreciationDetails}>
        <div className="parallelFields">
          <FormField
            isRequired
            type="text"
            name="assetName"
            title="Asset Name:"
            onChange={handleChange}
            value={assetDetails.assetName}
          />
          <FormField
            isRequired
            min="1"
            type="number"
            name="purchaseCost"
            onChange={handleChange}
            title="Purchase Cost ($):"
            value={assetDetails.purchaseCost}
          />
        </div>
        <div className="parallelFields">
          <FormField
            isRequired
            type="date"
            title="Purchase Date:"
            name="purchaseDate"
            value={assetDetails.purchaseDate}
            onChange={handleChange}
          />
          <FormField
            isRequired
            title="Category:"
            type="text"
            name="category"
            value={assetDetails.category}
            onChange={handleChange}
          />
        </div>
        <div className="singleFieldSection">
          <FormField
            min="0"
            type="number"
            title="Total Units of Production (If applicable):"
            name="totalUnitsOfProduction"
            value={assetDetails.totalUnitsOfProduction}
            onChange={handleChange}
          />
        </div>
        <Button
          text="Submit"
          type="submit"
          disable={isDisable}
          isLoading={isLoading}
        />
      </form>
      {depreciationDetails && (
        <DepreciationDetails details={depreciationDetails} />
      )}
    </div>
  );
};

export default Depreciation;
