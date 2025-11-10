# web - Frontend code

## Development

You should have read HACKING already.

Start development server using:

```
pnpm dev
vite dev
```

By default, Vite binds to the loopback interface on port 5173.
If it cannot bind to that, it will try 5714, and I guess it would
try 5715 next, and... I don't know.  I haven't tried that much.

Take port 5173 for example.  You want to access <http://localhost:5173/>.
(The host name is very significant.  **Do not use 127.0.0.1**.)

You can override these using `--host [host]` and `--port [port]`.


## Structure

Frontend HTML/CSS people, work on `src/lib/mod`,
which are concerned with UI components.

Frontend JavaScript people, work on `src/lib/sub`,
which are concerned with implementing these components.

Backend people you are in the wrong directory.
