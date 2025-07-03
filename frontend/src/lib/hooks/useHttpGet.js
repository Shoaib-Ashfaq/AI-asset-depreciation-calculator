import { http_get } from "src/lib/http";

const useHttpGet = () => {
  const httpGet = async (url) => {
    const response = await http_get(url);
    return response;
  };
  return httpGet;
};

export default useHttpGet;
