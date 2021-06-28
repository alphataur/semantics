## Intro to traits and crash course to display trait

```rust
struct Person{
    name: String,
    age: i64
}
impl std::fmt::Display for Person{
    fn fmt(&self, f: &mut std::fmt::Formatter) -> Result<(), std::fmt::Error>{
        write!(f, "{} {}", self.name, self.age)
    }
}
fn main(){
    let a = Person{name: String::from("Nikhil Surya Mukhi"), age: 24};
    println!("{}", a);
    println!("{}", "all is well");
}

}
```

here `&self` is an alias to self: &Self; where Self is the type of the struct.
