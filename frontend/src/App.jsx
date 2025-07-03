import {
  Navigate,
  Route,
  BrowserRouter as Router,
  Routes,
} from "react-router-dom";
import { Slide, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import Depreciation from "src/pages/Depreciation";
import Report from "src/pages/Report";

const App = () => {
  return (
    <Router>
      <ToastContainer
        theme="dark"
        transition={Slide}
        newestOnTop={true}
        position="bottom-right"
        autoClose={2000}
      />
      <Routes>
        <Route path="" element={<Depreciation />} />;
        <Route path="assets/:id" element={<Report />} />;
        <Route exact path="*" element={<Navigate to="/" />} />
      </Routes>
    </Router>
  );
};

export default App;
