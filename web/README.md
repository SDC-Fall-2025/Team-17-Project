# sv

Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```sh
# create a new project in the current directory
npx sv create

# create a new project in my-app
npx sv create my-app
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```sh
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.

## METAINFO

This directory was created with the following options:

```
$ pnpm dlx sv create frontend

┌  Welcome to the Svelte CLI! (v0.9.9)
│
◇  Directory not empty. Continue?
│  Yes
│
◇  Which template would you like?
│  SvelteKit minimal
│
◇  Add type checking with TypeScript?
│  Yes, using TypeScript syntax
│
◆  Project created
│
◇  What would you like to add to your project? (use arrow keys / space bar)
│  prettier, eslint, vitest, playwright, sveltekit-adapter
│
◇  vitest: What do you want to use vitest for?
│  unit testing, component testing
│
◇  sveltekit-adapter: Which SvelteKit adapter would you like to use?
│  vercel
│
◆  Successfully setup add-ons
│
◇  Which package manager do you want to install dependencies with?
│  pnpm
│
◆  Successfully installed dependencies
│
◇  Successfully formatted modified files
│
◇  What's next? ───────────────────────────────╮
│                                              │
│  📁 Project steps                            │
│                                              │
│    1: cd frontend                            │
│    2: pnpm run dev --open                    │
│                                              │
│  To close the dev server, hit Ctrl-C         │
│                                              │
│  Stuck? Visit us at https://svelte.dev/chat  │
│                                              │
├──────────────────────────────────────────────╯
│
└  You're all set!
```

An additional package [`sveletekit-i18n`](https://github.com/sveltekit-i18n/lib) was installed,
though it might have been a mistake...
