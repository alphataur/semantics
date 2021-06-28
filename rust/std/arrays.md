# rust arrays

static sized collection of a homogenous type(unlike python's list or javascript arrays).
by default immutatable without annotation mut.

contains the following traits
- Copy
- Clone
- Debug
- IntoIterator (implemented for [T; N], &[T; N] and &mut [T; N])
- PartialEq, PartialOrd, Eq, Ord
- Hash
- AsRef, AsMut
- Borrow, BorrowMut

### initialization
```rust
fn main(){
  let arr: [i64; 10] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  println!("{:?}", arr);
}
```



### initialization #2

lets initialize a array of 10 elements containing 100

```rust
fn main(){
  let arr: [i64; 10] = [100; 10];
  println!("{:?}", arr);
}
```

### iteration

```rust
fn main(){
  let arr: [i64; 10] = [100; 10];
  for i in arr.iter(){
    println!("{}", i)
  }
}
```

```rust
fn main(){
  let arr: [i64; 10] = [100; 10];
  for i in &arr(){
    println!("{}", i)
  }
}
```

### enumerated iteration

```rust
fn main(){
  let arr: [i64; 10] = [100; 10];
  for (index, value) in arr.iter().enumerate(){
    println!("{} with {}", index, value);
  }
}
```

### mutating inside a for loop

```rust
let mut arr: [i64; 10] = [10; 10];
let mut s = 0i64;
for i in arr.iter_mut(){
    *i = s;
    s += 1;
}
```

or idiomatically

```rust
let mut arr: [i64; 10] = [10; 10];
let mut s = 0i64;
for i in &mut arr{
    *i = s;
    s += 1;
}
```
