"use client";

import { useRouter } from 'next/navigation';

const ProfilePage = () => {
  const router = useRouter();

  const createReview = async (reviewData: { book_id: number; rating: number; review_text: string }) => {
    try {
      const response = await fetch('/api/reviews/create', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(reviewData),
      });

      if (response.ok) {
        const newReview = await response.json();
        console.log('Review created:', newReview);
      } else {
        console.error('Failed to create review');
      }
    } catch (error) {
      console.error('Error creating review:', error);
    }
  };

  const handleCreateReview = () => {
    createReview({
      book_id: 1,
      rating: 5,
      review_text: 'Amazing book, really enjoyed it!',
    });
  };

  const handleAddBook = () => {
    router.push('/add-book');
  };

  return (
    <div>
      <h1>Profile Page</h1>
      <button onClick={handleCreateReview}>Create Review</button>
      <button onClick={handleAddBook}>Add Book</button>
    </div>
  );
};

export default ProfilePage;
