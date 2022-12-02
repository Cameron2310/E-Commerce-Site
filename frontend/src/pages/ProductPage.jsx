import { useParams } from "react-router-dom";
import Product from "../components/Product";

export default function ProductPage({ props }) {
  return <Product props={props} />;
}
