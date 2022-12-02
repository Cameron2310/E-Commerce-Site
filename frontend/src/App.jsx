import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import HomePage from "./pages/HomePage";
import CategoryPage from "./pages/CategoryPage";
import NavBar from "./assets/components/NavBar";
import axios from "axios";

function App() {
  const [data, setData] = useState();

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios("http://localhost:8000/");
      setData(response.data);
    };
    fetchData();
  }, []);

  if (!data) {
    return null;
  }
  return (
    <Router>
      <NavBar props={data} />
      <Routes>
        <Route path="/" element={<HomePage props={data} />} />
        <Route path="/:category" element={<CategoryPage props={data} />} />
      </Routes>
    </Router>
  );
}

export default App;
