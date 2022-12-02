import React from "react";

export default function Summary({ props }) {
  return (
    <div className="col-lg-4 bg-grey">
      <div className="p-5">
        <h3 className="fw-bold mb-5 mt-2 pt-1">Summary</h3>
        <hr className="my-4"></hr>
        <div className="d-flex justify-content-between mb-4">
          {props.map((prop, i) => {
            return (
              <div key={i}>
                <h5 className="text-capitalize">{prop.name}</h5>
                <h5>$ {prop.cost}</h5>
              </div>
            );
          })}
        </div>
        <hr className="my-4" />
        <div className="d-flex justify-content-between mb-5">
          <h5 className="text-capitalize">Total price</h5>
          <h5>$ total cost</h5>
        </div>
      </div>
    </div>
  );
}
