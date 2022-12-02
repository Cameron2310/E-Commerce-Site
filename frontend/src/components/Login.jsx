import { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

export default function Login() {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();

  const getUser = async () => {
    const response = await axios("http://localhost:8000/login/", {
      params: {
        email: email,
        password: password,
      },
    });
    if (response.status == 200) {
      window.location = "/";
    } else {
      window.location = "login/";
    }
  };

  return (
    <div>
      <div>
        <input
          type="text"
          placeholder="Email"
          onChange={(e) => {
            setEmail(e.target.value);
          }}
        />
        <input
          type="text"
          placeholder="Password"
          onChange={(e) => {
            setPassword(e.target.value);
          }}
        />
      </div>
      <div>
        <button type="submit" onClick={getUser}>
          Login
        </button>
      </div>
      <Link to="signup/">New? Sign up for an account!</Link>
    </div>
  );
}
