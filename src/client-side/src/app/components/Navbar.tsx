import Link from 'next/link';
import './navbar.css';

export default function Navbar() {
  return (
    <nav className="navbar">
      <Link href="/register">
        <a className="nav-button">Register</a>
      </Link>
      <Link href="/login">
        <a className="nav-button">Login</a>
      </Link>
      <Link href="/add-book">
        <a className="nav-button">Add Book</a>
      </Link>
      <Link href="/profile">
        <a className="nav-button">Profile</a>
      </Link>
    </nav>
  );
}
