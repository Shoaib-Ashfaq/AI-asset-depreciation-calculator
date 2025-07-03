import { useEffect, useState } from "react";

import { fixed_to } from "src/lib/fixed_to";
import { i18n_number } from "src/lib/i18n_number";

const numberRegex = /^[+]?\d*\.?\d*$/;

const NumberInput = (props) => {
  const { title, min, max, value, onChange, ...rest } = props;
  const [v, setV] = useState(0);

  useEffect(() => {
    setV(fixed_to(value));
  }, [value]);

  const handleChange = (e) => {
    let val = e.target.value;
    val = val.replace(/,/g, "");
    if (numberRegex.test(val) || val === "") {
      var temp = parseFloat(val || "0");
      if (min && val < min) {
        temp = min;
      }
      if (max && val > max) {
        temp = max;
      }
      temp = fixed_to(temp);
      setV(temp);
      onChange(e.target.name, temp);
    }
  };

  return <input value={i18n_number(v)} onChange={handleChange} {...rest} />;
};

export default NumberInput;
