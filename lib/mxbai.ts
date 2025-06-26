import Mixedbread from "@mixedbread/sdk";
import dotenv from "dotenv";

dotenv.config();

const mxbai = new Mixedbread({
  apiKey: process.env.MXBAI_API_KEY ?? "",
});

export { mxbai };
