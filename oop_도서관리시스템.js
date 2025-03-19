// Book 클래스: 개별 책의 정보를 관리
class Book {
  static nextId = 1; // 자동 증가 ID를 위한 정적 변수

  constructor(title, author, year, category, price) {
    this.id = Book.nextId++; // 자동으로 고유 ID 생성
    this.title = title; // 제목
    this.author = author; // 저자
    this.year = year; // 출판 연도
    this.category = category; // 카테고리
    this.price = price; // 구매 가격
    this.isAvailable = true; // 대여 가능 여부 (기본값: true)
  }

  getDetails() {
    return `ID: ${this.id}, ${this.title} by ${this.author}, published in ${this.year}, Category: ${this.category}, Price: $${this.price}, Available: ${this.isAvailable ? "Yes" : "No"}`;
  }
}

// User 클래스: 사용자 정보를 관리
class User {
  static nextId = 1; // 자동 증가 ID를 위한 정적 변수

  constructor(name) {
    this.id = User.nextId++; // 자동으로 고유 ID 생성
    this.name = name; // 사용자 이름
    this.borrowedBooks = []; // 대여한 책 목록
    this.purchasedBooks = []; // 구매한 책 목록
  }

  borrowBook(book) {
    if (book.isAvailable) {
      book.isAvailable = false;
      this.borrowedBooks.push(book);
      console.log(`${this.name} borrowed "${book.title}".`);
    } else {
      console.log(`Sorry, "${book.title}" is currently not available for borrowing.`);
    }
  }

  returnBook(bookId) {
    const index = this.borrowedBooks.findIndex(book => book.id === bookId);
    if (index !== -1) {
      const returnedBook = this.borrowedBooks.splice(index, 1)[0];
      returnedBook.isAvailable = true;
      console.log(`${this.name} returned "${returnedBook.title}".`);
    } else {
      console.log(`No borrowed book with ID: ${bookId} found.`);
    }
  }

  purchaseBook(book) {
    if (book.isAvailable) {
      this.purchasedBooks.push(book);
      console.log(`${this.name} purchased "${book.title}" for $${book.price}.`);
    } else {
      console.log(`Sorry, "${book.title}" is currently not available for purchase.`);
    }
  }

  listBorrowedBooks() {
    if (this.borrowedBooks.length === 0) {
      console.log(`${this.name} has not borrowed any books.`);
    } else {
      console.log(`${this.name}'s Borrowed Books:`);
      this.borrowedBooks.forEach(book => console.log(book.getDetails()));
    }
  }

  listPurchasedBooks() {
    if (this.purchasedBooks.length === 0) {
      console.log(`${this.name} has not purchased any books.`);
    } else {
      console.log(`${this.name}'s Purchased Books:`);
      this.purchasedBooks.forEach(book => console.log(book.getDetails()));
    }
  }
}

// Library 클래스: 전체 도서 관리 시스템
class Library {
  constructor() {
    this.books = []; // 책 목록을 저장할 배열
  }

  addBook(book) {
    this.books.push(book);
    console.log(`"${book.title}" has been added to the library.`);
  }

  removeBookById(id) {
    const index = this.books.findIndex(book => book.id === id);
    if (index !== -1) {
      const removedBook = this.books.splice(index, 1)[0];
      console.log(`"${removedBook.title}" (ID: ${removedBook.id}) has been removed from the library.`);
    } else {
      console.log(`No book with ID: ${id} was found in the library.`);
    }
  }

  searchBookById(id) {
    const foundBook = this.books.find(book => book.id === id);
    if (foundBook) {
      console.log(`Found: ${foundBook.getDetails()}`);
      return foundBook;
    } else {
      console.log(`No book with ID: ${id} was found in the library.`);
      return null;
    }
  }

  searchBooksByCategory(category) {
    const booksInCategory = this.books.filter(book => book.category === category);
    if (booksInCategory.length > 0) {
      console.log(`Books in category "${category}":`);
      booksInCategory.forEach(book => console.log(book.getDetails()));
    } else {
      console.log(`No books found in category "${category}".`);
    }
  }

  listBooks() {
    if (this.books.length === 0) {
      console.log("The library is empty.");
    } else {
      console.log("Books in the library:");
      this.books.forEach(book => console.log(book.getDetails()));
    }
  }
}

// 시스템 테스트 코드

// 라이브러리 생성
const myLibrary = new Library();

// 새 책 추가 (ID는 자동 생성)
const book1 = new Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", 15);
const book2 = new Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 10);
const book3 = new Book("1984", "George Orwell", 1949, "Dystopian", 12);
const book4 = new Book("A Brief History of Time", "Stephen Hawking", 1988, "Science", 20);

myLibrary.addBook(book1);
myLibrary.addBook(book2);
myLibrary.addBook(book3);
myLibrary.addBook(book4);

// 사용자 생성 (ID는 자동 생성)
const user1 = new User("Alice");
const user2 = new User("Bob");

// 사용자 대여 및 구매 테스트
user1.borrowBook(myLibrary.searchBookById(1)); // Alice가 The Great Gatsby 대여
user1.purchaseBook(myLibrary.searchBookById(3)); // Alice가 1984 구매

user2.borrowBook(myLibrary.searchBookById(2)); // Bob이 To Kill a Mockingbird 대여

// 사용자 목록 출력
user1.listBorrowedBooks();
user1.listPurchasedBooks();

user2.listBorrowedBooks();

// 책 반환 테스트
user1.returnBook(1); // Alice가 The Great Gatsby 반환

// 라이브러리 상태 확인
myLibrary.listBooks();
