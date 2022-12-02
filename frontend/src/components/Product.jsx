import { useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import { e } from "mathjs";

export default function Product({ props }) {
  const { category, id } = useParams();

  function getCorrectData() {
    if (id === undefined) {
      const data = props.filter((prop, i) => {
        if (prop.category === category) {
          return props[i];
        }
      });
      return data;
    } else {
      const data = props.filter((prop, i) => {
        if (prop.id == id) {
          return props[i];
        }
      });
      return data;
    }
  }

  function goToProduct(id, category) {
    window.location = `/${category}/${id}/`;
  }

  if (id === undefined) {
    return (
      <div>
        {getCorrectData().map((datum, i) => {
          return (
            <Card style={{ width: "18rem" }} key={i}>
              <Card.Img variant="top" src={datum.image} />
              <Card.Body>
                <Card.Title>{datum.name}</Card.Title>
                <Card.Text>${datum.cost}</Card.Text>
                <Button
                  variant="primary"
                  onClick={() => goToProduct(datum.id, datum.category)}
                >
                  Go to Page
                </Button>
              </Card.Body>
            </Card>
          );
        })}
      </div>
    );
  } else {
    return (
      <div>
        {getCorrectData().map((datum, i) => {
          return (
            <Card style={{ width: "18rem" }} key={i}>
              <Card.Img variant="top" src={datum.image} />
              <Card.Body>
                <Card.Title>{datum.name}</Card.Title>
                <Card.Text>${datum.cost}</Card.Text>
                {/* <Button
                  variant="primary"
                  onClick={() => goToProduct(datum.id, datum.category)}
                >
                  Go to Page
                </Button> */}
              </Card.Body>
            </Card>
          );
        })}
      </div>
    );
  }
}
