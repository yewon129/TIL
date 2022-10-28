# JSX

> A Syntax extension to JavaScript

```jsx
const element = <h1>Hello, world!</h1>;
```



```jsx
#JSX 사용
const element = (
	<h1 className="greeting">Hello world</h1>
)

#JSX 미사용
const element = React.createElement(
    'h1',
    {className : 'greeting'},
    'Hello, world'
)
```

```jsx
React.createElement(
    type,
    [props],
    [...children])
```

