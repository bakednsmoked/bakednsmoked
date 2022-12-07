(async () => {
  let url: string;

  if (process.env.NODE_ENV === "production") {
    url = "http://localhost:8030/api/stock";
  } else {
    url = "http://localhost:5000/stock";
  }
  console.log(process.env.NODE_ENV);
  await fetch(url, {
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      mode: "cors",
    },
  })
    .then(async (msg) => {
      console.log(await msg.text());
    })
    .catch((err: Error) => {
      console.log(err);
    });
})();
