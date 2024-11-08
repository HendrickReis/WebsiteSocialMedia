from supabase import create_client, Client

url = "https://mlhiogitomxayaxfwwqq.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1saGlvZ2l0b214YXlheGZ3d3FxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMTA5NTg5NSwiZXhwIjoyMDQ2NjcxODk1fQ.XDzKlw5hgClTXelPxzD1aYO__m8DiaYRhFeiyCB_bFY"

supabase: Client = create_client(url, key)

mensagens = supabase.table("Mensagens").select("*").execute()

for c in mensagens.data:
    print(c)