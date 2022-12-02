import React from "react";
import { useState } from "react";

export default function Item({ props }) {
  const [quantity, setQuantity] = useState(0);
  return (
    <div className="row mb-4 d-flex justify-content-between align-items-center">
      <div className="col-md-2 col-lg-2 col-xl-2">
        <img
          src={props.image}
          className="img-fluid rounded-3"
          alt={props.name}
        />
      </div>
      <div className="col-md-3 col-lg-3 col-xl-3">
        <h5 className="text-muted">{props.category}</h5>
        <h5 className="text-black mb-0">{props.name}</h5>
      </div>
      <div className="col-md-3 col-lg-3 col-xl-2 d-flex">
        <form action="" method="post">
          <input
            id="form1"
            min="0"
            name="quantity"
            value={quantity}
            type="number"
            className="form-control form-control-sm"
            onChange={(e) => setQuantity(e.target.value)}
          />
          <input
            className="btn btn-primary"
            type="submit"
            value="Update Quantity"
          />
        </form>
      </div>
    </div>
  );
}
