/**
 * @param  {str in any case}
 * @returns string in title case
 */
export const convert_to_title_case = (str) => {
  return str
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join(" ");
};
