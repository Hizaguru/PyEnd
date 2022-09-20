import React, { useState, useEffect, useRef } from "react";

export const Login = () => {
  const useRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState("");

  return <div>Login</div>;
};
