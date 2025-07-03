import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

import "src/pages/Depreciation.css";
import Button from "src/lib/components/Button";
import FormField from "src/lib/components/FormField";
import useHttpPost from "src/lib/hooks/useHttpPost";

const DepreciationDetails = ({ details }) => {
  const [isLoading, setIsLoading] = useState(false);
  const [formData, setFormData] = useState({
    asset_id: details.asset_id,
    useful_life: details.useful_life,
    depreciation_method: details.depreciation_method,
    salvage_value: details.salvage_value,
    total_units_of_production: details.total_units_of_production,
  });
  const isUnitsOfProduction =
    formData.depreciation_method === "Units of Production";
  const [annualProduction, setAnnualProduction] = useState(
    details.total_units_of_production / details.useful_life
  );

  const navigate = useNavigate();
  const httpPost = useHttpPost();

  const handleChange = (name, value) => {
    var tempV = value;
    var tempN = name;
    if (name === "annual_units_of_production") {
      setAnnualProduction(value);
      tempN = "useful_life";
      tempV = formData.total_units_of_production / value;
    } else if (name === "useful_life") {
      setAnnualProduction(formData.total_units_of_production / value);
    } else if (name === "depreciation_method") {
      if (value === "Units of Production") {
        setFormData({
          ...formData,
          useful_life: details.useful_life,
          depreciation_method: tempV,
        });
        setAnnualProduction(
          details.total_units_of_production / details.useful_life
        );
        return;
      } else {
        setAnnualProduction(0);
      }
    }
    setFormData({
      ...formData,
      [tempN]: tempV,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Ensure total units of production if method is units of production.
    if (!details.total_units_of_production && isUnitsOfProduction) {
      toast.error(
        "The depreciation method cannot be 'Units of Production' without providing the total units of production."
      );
      return;
    }

    setIsLoading(true);
    const resp = await httpPost("http://localhost:8000/api/upd-asset", {
      id: formData.asset_id,
      useful_life: formData.useful_life,
      salvage_value: formData.salvage_value,
      depreciation_method: formData.depreciation_method,
      annual_units_of_production: annualProduction,
    });
    setIsLoading(false);
    if (resp.code === 200) {
      toast.success("Updated successfully.");
      navigate(`/assets/${formData.asset_id}`);
    } else {
      toast.error(
        "We are facing some issues right now. Please try again later."
      );
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit} style={{ marginTop: "30px" }}>
        <h3>Depreciation Details</h3>
        <div className="parallelFields">
          <FormField
            isRequired
            min="1"
            max={isUnitsOfProduction ? formData.total_units_of_production : ""}
            type="number"
            name="useful_life"
            onChange={handleChange}
            title="Useful Life (Years):"
            value={formData.useful_life}
          />
          <FormField
            isRequired
            min="0"
            name="salvage_value"
            type="number"
            onChange={handleChange}
            title="Salvage Value ($):"
            value={formData.salvage_value}
          />
        </div>
        <div className="parallelFields">
          <div
            className={`singleFieldSection ${
              isUnitsOfProduction ? "fullWidth" : ""
            }`}
          >
            <label>Depreciation Method:</label>
            <select
              name="depreciation_method"
              value={formData.depreciation_method}
              onChange={(e) => {
                const { name, value } = e.target;
                handleChange(name, value);
              }}
              required
            >
              <option value="">Select Method</option>
              <option value="Straight Line">Straight Line</option>
              <option value="Double Declining Balance">
                Double Declining Balance
              </option>
              <option value="Units of Production">Units of Production</option>
              <option value="Sum of Years Digits">Sum of Years Digits</option>
            </select>
          </div>
          {isUnitsOfProduction && (
            <FormField
              isRequired
              min="1"
              max={formData.total_units_of_production}
              name="annual_units_of_production"
              type="number"
              onChange={handleChange}
              title="Annual Units of Production:"
              value={annualProduction}
            />
          )}
        </div>
        <Button text="Approve" type="submit" isLoading={isLoading} />
      </form>
    </>
  );
};

export default DepreciationDetails;
