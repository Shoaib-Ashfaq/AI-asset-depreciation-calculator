import "src/lib/components/Button.css";

const Button = (props) => {
  const { isLoading, text, disable, ...rest } = props;

  return (
    <button className="customButton" disabled={disable || isLoading} {...rest}>
      {isLoading ? <div className="spinner"></div> : text}
    </button>
  );
};

export default Button;
