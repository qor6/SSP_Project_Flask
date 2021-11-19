import { render, screen } from '@testing-library/react';
import App from 'C:\Users\mom42\PycharmProjects\SSP_Project_React/App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
