import { useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";

export default function Product({ props }) {
  const { category } = useParams();
  const data = props.filter((prop, i) => {
    if (prop.category === category) {
      return props[i];
    }
  });
  return (
    <div>
      {data.map((datum, i) => {
        return (
          <Card style={{ width: "18rem" }} key={i}>
            <Card.Img variant="top" src={datum.image} />
            <Card.Body>
              <Card.Title>{datum.name}</Card.Title>
              <Card.Text>${datum.cost}</Card.Text>
              <Button variant="primary">Go to Page</Button>
            </Card.Body>
          </Card>
        );
      })}
    </div>
  );
}
