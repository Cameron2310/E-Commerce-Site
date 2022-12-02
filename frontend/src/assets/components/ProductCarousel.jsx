import Carousel from "react-bootstrap/Carousel";

export default function ProductCarousel({ props }) {
  return (
    <div>
      <Carousel>
        {props.map((prop, i) => {
          return (
            <Carousel.Item key={i}>
              <img className="d-block w-100" src={prop.image} alt={prop.name} />
            </Carousel.Item>
          );
        })}
      </Carousel>
    </div>
  );
}
