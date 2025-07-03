export const http_common = async (method, url, body) => {
  const opts = {
    method,
    mode: "cors",
    cache: "no-cache",
    headers: {
      "Content-Type": "application/json",
    },
  };
  if (body) {
    opts.body = JSON.stringify(body);
  }
  const resp = await fetch(url, opts);

  try {
    const data = await resp.json();
    return { code: resp.status, error:data.detail, data };
  } catch (err) {
    console.error("http_common: not json:", err);
    return { code: resp.status };
  }
};

export const http_get = async (url) => {
  return http_common("GET", url);
};

export const http_post = async (url, body) => {
  return http_common("POST", url, body);
};
