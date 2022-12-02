import Summary from "./Summary";
import Item from "./Item";
import { useState, useEffect } from "react";
import axios from "axios";

export default function ShoppingCart() {
  const [items, setItems] = useState();

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios("http://localhost:8000/cart/");
      setItems(response.data[0].items);
    };
    fetchData();
  }, []);

  if (items === undefined) return null;
  return (
    // <!-- https://mdbootstrap.com/docs/standard/extended/shopping-carts/#! -->
    <section className="h-100 h-custom" style={{ backgroundColor: "#d2c9ff" }}>
      <div className="container py-5 h-100">
        <div className="row d-flex justify-content-center align-items-center h-100">
          <div className="col-12">
            <div
              className="card card-registration card-registration-2"
              style={{ borderRadius: "15px" }}
            >
              <div className="card-body p-0">
                <div className="row g-0">
                  <div className="col-lg-8">
                    <div className="p-5">
                      <div className="d-flex justify-content-between align-items-center mb-5">
                        <h1 className="fw-bold mb-0 text-black">
                          Shopping Cart
                        </h1>
                      </div>
                      <hr className="my-4" />
                      {items.map((item, i) => {
                        return <Item props={item} key={i} />;
                      })}
                    </div>
                  </div>
                  <Summary props={items} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
