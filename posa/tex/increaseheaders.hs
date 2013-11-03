import Text.Pandoc

behead :: Block -> Block
behead (Header n b xs) = Header (n + 1) b xs
behead x = x

transformDoc :: Pandoc -> Pandoc
transformDoc = bottomUp behead

readDoc :: String -> Pandoc
readDoc = readMarkdown def

writeDoc :: Pandoc -> String
writeDoc = writeMarkdown def

main :: IO ()
main = interact (writeDoc . transformDoc . readDoc)
