import React, { useState, useEffect, useRef } from "react";

export const Login = () => {
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState("");


  useEffect(() => {
    userRef.current.focus()
    setErrMsg('');
  }, [user, pwd])

  const handleSubmit = async (e) => {
    e.preventDefault(user, pwd);
    setUser('')
    setPwd('')
    setSuccess(true);

  }

  return (

    <section>
      <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">
        {errMsg}
      </p>
      <h1>Sign in</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input type="text"
          id="username"
          ref={userRef}
          autoComplete="off"
          onChange={(e) => setUser(e.target.value)}
          value={user} />
        <label htmlFor="password">Password:</label>
        <input type="text"
          id="username"
          ref={userRef}
          onChange={(e) => setPwd(e.target.value)}
          value={pwd} />
      </form>
      <button>Sign in</button>
    </section>

  )
};
