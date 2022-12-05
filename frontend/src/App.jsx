import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";

import NavBar from "./components/NavBar";
import HomePage from "./pages/HomePage";
import CategoryPage from "./pages/CategoryPage";
import ProductPage from "./pages/ProductPage";
import LoginPage from "./pages/LoginPage";
import SignUpPage from "./pages/SignUpPage";
import ShoppingCartPage from "./pages/ShoppingCartPage";
import NotFound from "./pages/NotFound";
import axios from "axios";

function App() {
  const [data, setData] = useState();

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios("http://localhost:8000/products/");
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
        <Route path="/:category/" element={<CategoryPage props={data} />} />
        <Route path="/:category/:id/" element={<ProductPage props={data} />} />
        <Route path="/login/" element={<LoginPage props={data} />} />
        <Route path="login/signup/" element={<SignUpPage />} />
        <Route path="/shopping-cart" element={<ShoppingCartPage />} />
        <Route path="*" element={<NotFound props={data} />} />
      </Routes>
    </Router>
  );
}

export default App;
