/**
 * @param  {number}
 * @returns number with decimal fixed
 */
export const fixed_to = (number, n = 2) => {
  return number % 1 !== 0 && number.toString().split(".")[1]?.length > 2
    ? number.toFixed(n)
    : number;
};
