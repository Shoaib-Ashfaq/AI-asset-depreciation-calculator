import "src/lib/components/FormField.css";
import NumberInput from "src/lib/components/NumberInput";

const FormField = (props) => {
  const { title, type, value, onChange, isRequired, ...rest } = props;

  return (
    <div className="fieldSection">
      <label>
        {title}
        <span>{isRequired && "*"}</span>
      </label>
      {type === "number" ? (
        <NumberInput
          required={isRequired}
          {...{ value, onChange, title }}
          {...rest}
        />
      ) : (
        <input
          required={isRequired}
          {...{ type, value }}
          onChange={(e) => {
            const { value, name } = e.target;
            onChange(name, value);
          }}
          {...rest}
        />
      )}
    </div>
  );
};

export default FormField;
