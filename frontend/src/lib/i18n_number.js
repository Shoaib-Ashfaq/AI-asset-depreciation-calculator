/**
 * @param  {number || string}
 * @returns string
 */
export const i18n_number = (value) => {
    return value.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, '$1,');
};
