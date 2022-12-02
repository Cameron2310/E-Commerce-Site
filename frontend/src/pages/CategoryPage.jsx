// import { useParams } from "react-router-dom";
import Product from "../components/Product";

export default function CategoryPage({ props }) {
  return (
    <div>
      <Product props={props} />
    </div>
  );
}
