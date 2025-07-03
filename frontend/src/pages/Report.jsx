import { useEffect, useState } from "react";
import { useParams } from "react-router";
import { toast } from "react-toastify";

import "./Reports.css";
import { fixed_to } from "src/lib/fixed_to";
import useHttpGet from "src/lib/hooks/useHttpGet";
import { i18n_number } from "src/lib/i18n_number";
import { isValidUUID } from "src/lib/is_valid_uuid";
import { convert_to_title_case } from "src/lib/title_case";

const DetailsCard = (props) => {
  const { label, value } = props;

  return (
    <div className="detail_card">
      <p className="label">{label}</p>
      <p className="value">{value}</p>
    </div>
  );
};

const Report = () => {
  const [asset, setAsset] = useState({
    name: "",
    purchase_cost: "",
    purchase_date: "",
    category: "",
    useful_life: "",
    salvage_value: "",
    depreciation_method: "",
    report: [],
  });

  const httpGet = useHttpGet();
  const { id } = useParams();

  const getReport = async () => {
    if (!isValidUUID(id)) {
      toast.error("Invalid Asset ID");
      return;
    }

    let toastType = "";
    let toastMsg = "Getting report...";
    const t = toast.loading(toastMsg);

    const resp = await httpGet(
      `http://localhost:8000/api/get-asset/?asset_id=${id}`
    );
    if (resp.code === 200) {
      const data = resp.data;
      setAsset({
        name: data.name,
        purchase_cost: data.purchase_cost,
        purchase_date: data.purchase_date,
        category: data.category,
        useful_life: data.useful_life,
        salvage_value: data.salvage_value,
        depreciation_method: data.depreciation_method,
        report: data.report,
        annual_units_of_production: data.annual_units_of_production,
        total_units_of_production: data.total_units_of_production,
      });
      toastType = "success";
      toastMsg = "Report Generated!";
    } else {
      toastType = "error";
      if (resp.error) {
        toastMsg = resp.error;
      } else {
        toastMsg =
          "We are facing some issues right now. Please try again later.";
      }
    }
    toast.update(t, {
      render: toastMsg,
      type: toastType,
      isLoading: false,
      autoClose: true,
    });
  };

  useEffect(() => {
    getReport();
  }, []);

  return (
    <>
      <div className="container">
        <button className="backBtn" onClick={() => window.history.go(-1)}>
          <span className="arrow">«</span> Go Back
        </button>
        <h1>Depreciation Report</h1>
        <h2>Asset Details</h2>
        <section className="details_section">
          <DetailsCard
            label="Asset Name:"
            value={convert_to_title_case(asset.name)}
          />
          <DetailsCard
            label="Purchase Cost ($):"
            value={`${i18n_number(asset.purchase_cost)}`}
          />
          <DetailsCard label="Purchase Date:" value={asset.purchase_date} />
          <DetailsCard
            label="Category:"
            value={convert_to_title_case(asset.category)}
          />
          <DetailsCard
            label="Useful Life (Years):"
            value={`${asset.useful_life}`}
          />
          <DetailsCard
            label="Salvage Value ($):"
            value={`${i18n_number(asset.salvage_value)}`}
          />
          <DetailsCard
            label="Depreciation Method:"
            value={asset.depreciation_method}
          />
          {asset.depreciation_method === "Units of Production" && (
            <>
              <DetailsCard
                label="Total Units of Production:"
                value={i18n_number(fixed_to(asset.total_units_of_production))}
              />
              <DetailsCard
                label="Annual Units of Production:"
                value={i18n_number(fixed_to(asset.annual_units_of_production))}
              />
            </>
          )}
        </section>
        <h2 style={{ marginTop: "30px" }}>Depreciation Schedule</h2>
        <table className="report_table">
          <thead>
            <tr>
              <th>Year</th>
              <th>Annual Depreciation ($)</th>
              <th>Accumulated_Depreciation ($)</th>
              <th>Book Value ($)</th>
            </tr>
          </thead>
          <tbody>
            {asset.report?.map((item, index) => (
              <tr key={index}>
                <td>{item.year}</td>
                <td>{i18n_number(fixed_to(item.annual_depreciation))}</td>
                <td>{i18n_number(fixed_to(item.accumulated_depreciation))}</td>
                <td>{i18n_number(fixed_to(item.book_value))}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
};

export default Report;
