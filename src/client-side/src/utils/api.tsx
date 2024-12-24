import axios from "axios";

const API_URL = "http://localhost:8000";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const register = async (userData: { name: string; email: string; password: string }) => {
  return api.post("/users/register", userData);
};


export const login = async (userData: { email: string; password: string }) => {
  return api.post("/users/login", userData);
};

export const createBook = async (bookData: FormData) => {
  return api.post("/books/create-book", bookData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};

export const getBook = async (bookId: number) => {
  return api.get(`/books/get-book/${bookId}`);
};

export const deleteBook = async (bookId: number) => {
  return api.delete(`/books/delete-book/${bookId}`);
};

export const getReviews = async (bookId: number) => {
  return api.get(`/reviews/${bookId}`);
};

export const createReview = async (reviewData: { book_id: number; rating: number; review_text: string }) => {
  return api.post("/reviews", reviewData);
};

export const getUserProfile = async () => {
  return api.get("/users/profile");
};
