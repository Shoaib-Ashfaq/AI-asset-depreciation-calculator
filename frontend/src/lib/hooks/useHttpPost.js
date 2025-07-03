import { http_post } from "src/lib/http";

const useHttpPost = () => {
  const httpPost = async (url, body) => {
    const response = await http_post(url, body);
    return response;
  };
  return httpPost;
};

export default useHttpPost;
