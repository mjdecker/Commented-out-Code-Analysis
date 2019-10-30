    int x, y;   
                               m14));
                      encoding_prefix(tok->enc),
                      encoding_prefix(tok->enc),
                      quote_char(tok->c));
                      quote_cstring(tok->sval));
                      ty2s(node->ty), node2s(node));
                    break;
                    break;
                    buf_printf(b, ",");
                    emit("mov %d(#rbp), #al", arg++ * 8);
                    emit("mov %d(#rbp), #rax", arg++ * 8);
                    emit("movzb #%s, #%s", SREGS[ireg], MREGS[ireg]);
                    emit("movzb #al, #eax");
                    vec_append(r, arg);
                    vec_pop(r);
                    vec_push(r, vec_get(arg, i));
                   node->declvar->varname);
                   node->kind == AST_FUNCALL ? node->fname : node2s(node));
                   node2s(node->cond),
                   node2s(node->cond),
                   node2s(node->els));
                   node2s(node->operand));
                   node2s(node->then));
                   node2s(node->then),
                   ty2s(node->declvar->ty),
                   ty2s(node->operand->ty),
                   ty2s(node->ty),
                  2 +) 10);
                 float v06, float v07, float v08, float v09, float v10,
                 float v11, float v12, float v13, float v14, float v15,
                 float v16, float v17) {
                *p = ' ';
                17.0);
                9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0,
                align = val;
                arg->ty;
                base = base->operand;
                break;
                break;
                break;
                break;
                buf_printf(b, " (%s)", do_ty2s(dict, fieldtype));
                buf_printf(b, "%s", do_ty2s(dict, t));
                buf_printf(b, ",");
                buf_printf(b, ",");
                char *key = vec_get(keys, i);
                char *s = vec_get(keys, i++);
                col += TAB - 1;
                continue;
                continue;
                continue;
                continue;
                continue;
                data |= ((((long)1 << totype->bitsize) - 1) & eval_intexpr(v, NULL)) << totype->bitoff;
                else
                emit(".quad %u", v);
                emit("mov %d(#rbp), #rax", arg++ * 8);
                error("flexible member may only appear as the last member: %s %s", ty2s(ty), name);
                error("flexible member with no other fields: %s %s", ty2s(ty), name);
                error("global variable expected, but got %s", node2s(base));
                error("pointer type expected, but got %s %s",
                errort(tok, ", expected, but got %s", tok2s(tok));
                errort(tok, "array designator exceeds array bounds: %d", idx);
                errort(tok, "at least one parameter is required before \"...\"");
                errort(tok, "default expression specified twice");
                errort(tok, "field does not exist: %s", tok2s(tok));
                errort(tok, "function expected, but got %s", node2s(node));
                errort(tok, "malformed desginated initializer: %s", tok2s(tok));
                errort(tok, "negative alignment: %d", val);
                expect(';');
                fieldtype->bitoff = 0;
                fieldtype->bitoff = bitoff;
                fieldtype->offset = off;
                fieldtype->offset = off;
                finish_bitfield(&off, &bitoff);
                for (int i = 1; i < vec_len(arg); i++)
                glue_push(r, vec_head(arg));
                goto errcheck;
                i++;
                if (i > 0)
                if (node->totype->bitsize <= 0) {
                if (strcmp(fieldname, s) == 0)
                if (usertype) goto err;
                if (v->ty->kind == KIND_BOOL)
                if (v->ty->kind == KIND_BOOL) {
                if (vec_len(arg) > 0)
                is_inttype(arg->ty) ? type_int :
                m->nused++;
                node = vec_get(inits, i);
                off += compute_padding(off, fieldtype->align);
                push("rax");
                push("rax");
                push(REGS[ireg++]);
                push_xmm(xreg++);
                return c;
                return false;
                subst = copy_token(subst);
                subst->space = tok->space;
                totype = node->totype;
                Type *fieldtype = dict_get(ty->fields, key);
                Type *t = vec_get(ty->params, i);
                unget_token(tok);
                unget_token(tok);
                usertype = def;
                v = node->initval;
                vec_append(r, arg);
                vec_push(block, ast_decl(var, NULL));
                vec_push(block, ast_decl(var, read_decl_init(ty)));
                vec_push(r, subst);
                warnt(peek(), "missing ';' at the end of field list");
                }
                }
                } else {
             float:F, double:D, ldouble:LD)
            "One of -a, -c, -E or -S must be specified.\n\n");
            "Usage: 8cc [ -E ][ -a ] [ -h ] <file>\n\n"
            *addr = conv(node);
            *align = MAX(*align, fieldtype->align);
            *defaultexpr = read_assignment_expr();
            *ellipsis = true;
            *end = true;
            *q++ = *p++;
            *q++ = *p++;
            a2s_declinit(b, node->declinit);
            a2s_declinit(b, node->lvarinit);
            arg += size / 8;
            arg = ast_conv(paramtype, arg);
            assert(node->totype->bitoff == 0);
            assert(param->kind == AST_LVAR);
            assert(ty->ptr);
            assign_string(inits, ty, tok->sval, off);
            assign_string(inits, ty, tok->sval, off);
            ast_typedef(ty, name);
            bitoff += fieldtype->bitsize;
            bitoff = 0;
            buf[i++] = '%';
            buf[i++] = '%';
            buf[i++] = *p;
            buf_printf(b, " %s", node2s(node->els));
            buf_printf(b, " -> ");
            buf_printf(b, "%d", node->ival);
            buf_printf(b, "%f", node->fval);
            buf_printf(b, "%ldL", node->ival);
            buf_printf(b, "%lldL", node->ival);
            buf_printf(b, "%s %s", ty2s(param->ty), node2s(param));
            buf_printf(b, "%s", node2s(vec_get(node->args, i)));
            buf_printf(b, "(");
            buf_printf(b, "(%c ", node->kind);
            buf_printf(b, "(%s", kind);
            buf_printf(b, "(== ");
            buf_printf(b, ")");
            buf_printf(b, ")");
            buf_printf(b, ";");
            buf_printf(b, "\"%s\"", quote_cstring(node->sval));
            buf_printf(cppdefs, "#define %s\n", optarg);
            buf_printf(cppdefs, "#undef %s\n", optarg);
            buf_write(b, ' ');
            Buffer *b = make_buffer();
            char *name = NULL;
            char *p = strchr(optarg, '=');
            close_file(vec_pop(files));
            designated = true;
            designated = true;
            dict_put(r, name, fieldtype);
            dict_put(r, name, fieldtype);
            do_emit_data(v->lvarinit, v->ty->size, 0, depth);
            do_node2s(b, vec_get(node->stmts, i));
            else buf_printf(b, "'%c'", node->ival);
            else goto err;
            else if (node->ival == '\0') buf_printf(b, "'\\0'");
            else if (node->ival == '\\') buf_printf(b, "'\\\\'");
            else if (size == klong) size = kllong;
            emit(".long %d", *(uint32_t *)&fval);
            emit(".quad %lu", *(uint64_t *)&node->fval);
            emit(".quad %s", val->glabel);
            emit(".quad %s", val->newlabel);
            emit(".quad %s+%u", base->glabel, v * ty->ptr->size);
            emit(".string \"%s\"", quote_cstring_len(node->sval, node->ty->size - 1));
            emit("lea %d(#rbp), #rax", arg * 8);
            emit("lea %s(#rip), #rax", label);
            emit("lea %s+%d(#rip), #rax", label, off);
            emit("mov #edx, #eax");
            emit("ucomisd #xmm0, #xmm1");
            emit("ucomiss #xmm0, #xmm1");
            emit_addr(v);
            emit_data_addr(v->operand, depth);
            emit_data_charptr(val->operand->sval, depth);
            emit_data_primtype(totype, &(Node){ AST_LITERAL, totype, .ival = data }, depth);
            emit_expr(node->initval);
            emit_expr(v);
            emit_expr(v);
            emit_label(node->flabel);
            emit_label(node->flabel);
            emit_label(node->newlabel);
            emit_label(node->slabel);
            emit_lsave(node->totype, node->initoff + off);
            emit_noindent(".data");
            emit_noindent(".text");
            emit_noindent(".text");
            emit_noindent(".text");
            emit_save_literal(node->initval, node->totype, node->initoff + off);
            emit_toplevel(v);
            emit_zero_filler(lastend + off, node->initoff + off);
            enc = enc2;
            ensure_lvalue(node);
            ensure_lvalue(node);
            ensure_not_void(fieldtype);
            ensure_not_void(ty);
            ensure_not_void(ty);
            error("as failed");
            error("declarations of %s does not match", tag);
            error("duplicate case value: %d", x->beg);
            error("internal error");
            error("invalid pointer arith");
            error("invalid UTF-8 continuation byte");
            error("premature end of input");
            error("premature end of input");
            error("premature end of input");
            error("stray %s: %s", src->kind == AST_GOTO ? "goto" : "unary &&", label);
            errort(hash, "premature end of header name");
            errort(ident, "unterminated macro argument list");
            errort(name, "missing ')' in macro parameter list");
            errort(peek(), "';' or ',' are expected, but got %s", tok2s(peek()));
            errort(peek(), "K&R-style declarator expected, but got %s", tok2s(peek()));
            errort(tok, "case region is not in correct order: %d ... %d", beg, end);
            f->p++;
            fieldname = tok->sval;
            fieldname = vec_get(keys, i++);
            fieldtype = copy_type(fieldtype);
            fieldtype = dict_get(ty->fields, fieldname);
            fieldtype = dict_get(ty->fields, fieldname);
            fieldtype->bitoff = 0;
            fieldtype->bitsize = next_token(':') ? read_bitsize(name, fieldtype) : -1;
            fieldtype->offset = off;
            finish_bitfield(&off, &bitoff);
            finish_bitfield(&off, &bitoff);
            finish_bitfield(&off, &bitoff);
            float fval = node->fval;
            for (i++ ; i < vec_len(inits); i++) {
            for (int i = 0; i < vec_len(keys); i++) {
            for (int i = 0; i < vec_len(ty->params); i++) {
            for (q--; q[-1] != '/'; q--);
            functype->hasva = false;
            get();
            glue_push(r, t1);
            hideset = t1->hideset;
            hideset = t1->hideset;
            i = 0;
            i = idx;
            i++;
            i++;
            i++;
            if (!fieldtype)
            if (!has_brace)
            if (!has_brace)
            if (!is_keyword(tok, ','))
            if (!is_same_struct(vec_get(ka, i), vec_get(kb, i)))
            if (!tok || tok->kind != TIDENT)
            if (*defaultexpr)
            if (*p == '\t')
            if (align == -1 || val < align)
            if (base == NULL) {
            if (base->kind != AST_GVAR)
            if (base->kind == AST_CONV || base->kind == AST_ADDR)
            if (def) {
            if (fieldtype->bitsize <= room) {
            if (i != vec_len(fields) - 1)
            if (i == vec_len(inits))
            if (i == vec_len(keys))
            if (i > 0)
            if (i > 0)
            if (idx < 0 || (!flexible && ty->len <= idx))
            if (ireg >= 6) {
            if (is_keyword(peek(), '}'))
            if (k == NULL)
            if (k[j] != NULL)
            if (next_token(','))
            if (next_token('=')) {
            if (node->ival == '\n')      buf_printf(b, "'\n'");
            if (node->ty->kind != KIND_PTR)
            if (p)
            if (q == buf + 1)
            if (size == 0) size = klong;
            if (strcmp(param->varname, var->varname))
            if (subst) {
            if (t->kind != KIND_PTR || t->ptr->kind != KIND_FUNC)
            if (t1->is_vararg && vec_len(r) > 0 && is_keyword(vec_tail(r), ',')) {
            if (usertype) goto err;
            if (val < 0)
            if (val == 0)
            if (vec_len(arg) == 0)
            if (vec_len(fields) == 1)
            if (vec_len(files) == 1)
            if (vec_len(types) == 0)
            if (xreg >= 8) {
            init = ast_conv(ty, init);
            int bit = fieldtype->size * 8;
            int idx = read_intexpr();
            int op = is_keyword(tok, OP_INC) ? OP_POST_INC : OP_POST_DEC;
            int room = bit - (off * 8 + bitoff) % bit;
            int size = push_struct(v->ty->size);
            int v = eval_intexpr(val, &base);
            int val = read_alignas();
            is_same_struct(a->ptr, b->ptr);
            k[j] = m->key[i];
            keys = dict_keys(ty->fields);
            len++;
            len++;
            level++;
            level--;
            long data = eval_intexpr(v, NULL);
            m->key[i] = key;
            m->nelem++;
            m->val[i] = val;
            m->val[i] = val;
            MACRO_FUNC, .nargs = nargs, .body = body, .is_varg = is_varg });
            map_put(param, "__VA_ARGS__", make_macro_token(pos++, true));
            map_put(param, arg, make_macro_token(pos++, true));
            map_put(tags, tag, r);
            Node *base = NULL;
            Node *expr = read_assignment_expr();
            Node *node = read_compound_literal(ty);
            Node *param = vec_get(node->params, i);
            Node *param = vec_get(params, j);
            Node *var = (isglobal ? ast_gvar : ast_lvar)(ty, name);
            node = ast_uop(AST_DEREF, node->ty->ptr, node);
            node = conv(node);
            node = read_funcall(node);
            node = read_struct_field(node);
            node = read_struct_field(node);
            node = read_subscript_expr(node);
            node->flabel = make_label();
            node->flabel = make_label();
            node->slabel = make_label();
            numfp++;
            numgp++;
            off += compute_padding(off, fieldtype->align);
            off += compute_padding(off, fieldtype->align);
            off += compute_padding(off, fieldtype->align);
            off += fieldtype->size;
            off += fieldtype->size;
            off += node->totype->size;
            off += totype->size;
            off -= 8;
            off -= 8;
            off -= size;
            op = node->ty->usig ? OP_SHR : OP_SAR;
            op = OP_SAL;
            outfile = replace_suffix(base(infile), 'o');
            p += 2;
            p += 2;
            p += 2;
            p += 3;
            p++;
            p[0] = '\0';
            p[0] = '\0';
            param->ty = var->ty;
            paramtype = is_flotype(arg->ty) ? type_double :
            paramtype = vec_get(params, i++);
            perror("execl failed");
            perror("mkstemps");
            printf(" ");
            printf("%s", node2s(v));
            printf("\n");
            push("rax");
            push_xmm(0);
            r += 8;
            r += 8;
            r += push_struct(v->ty->size);
            r = make_rectype(is_struct);
            r = set_add(r, a->v);
            r = set_add(r, a->v);
            r[i++] = p + 1;
            r[i++] = p;
            read_decl(toplevels, true);
            realloc_body(b);
            realloc_body(b);
            right = ast_conv(node->ty, right);
            rtype = lastexpr->ty;
            size -= node->totype->size;
            size -= totype->size;
            skip_parentheses(buf);
            skip_parentheses(buf);
            squash_unnamed_struct(r, fieldtype, 0);
            squash_unnamed_struct(r, fieldtype, off);
            src->newlabel = dst->newlabel = make_label();
            src->newlabel = dst->newlabel;
            struct { char c[8]; } y;
            struct { char c[8]; };
            struct { int a; int b; } x;
            struct { int x; int y; };
            tok = copy_token(tok);
            tok = get();
            tok = get();
            tok = lex();
            tok->bol = false;
            tok->space = true;
            Token *subst = map_get(param, tok->sval);
            Token *tok = peek();
            Token *tok = peek();
            ty->len = 0;
            ty->size = 0;
            Type *def = get_typedef(tok->sval);
            Type *fieldtype = read_declarator(&name, basetype, NULL, DECL_PARAM_TYPEONLY);
            Type *t = node->ty;
            Type *totype = node->totype;
            Type *ty = base->ty;
            Type *ty = read_cast_type();
            usertype = read_typeof();
            v[j] = m->val[i];
            val = read_intexpr();
            vec_append(r, expand_all(arg, t0));
            vec_push((ireg++ < imax) ? ints : rest, v);
            vec_push((xreg++ < xmax) ? floats : rest, v);
            vec_push(list, stmt);
            vec_push(r, cpp_token_zero);
            vec_push(r, make_pair(name, fieldtype));
            vec_push(r, make_pair(NULL, basetype));
            vec_push(r, make_pair(ty, expr));
            vec_push(r, read_defined_op());
            vec_push(r, stringize(t0, vec_get(args, t1->position)));
            vec_push(r, tok);
            vec_push(rest, v);
            vec_push(toplevels, read_funcdef());
            vec_push(vars, ast_lvar(ty, name));
            Vector *arg = vec_get(args, t0->position);
            Vector *arg = vec_get(args, t0->position);
            Vector *arg = vec_get(args, t1->position);
            Vector *keys = dict_keys(ty->fields);
            while (i < vec_len(keys)) {
            write16(b, (rune & 0x3FF) + 0xDC00);
            write16(b, (rune >> 10) + 0xD7C0);
            write16(b, rune);
            }
            }
            }
            }
            }
            }
            }
            }
            }
            }
            }
            }
            } else if (sclass != S_EXTERN && ty->kind != KIND_FUNC) {
            } else if (vec_len(arg) > 0) {
            } else {
            } else {
            } else {
            } while ((count -= 8) > 0);
        for (int i = 0; i < vec_len(node->args); i++) {
        for (int i = 0; i < vec_len(node->params); i++) {
        for (int i = 0; i < vec_len(node->stmts); i++) {
        for (int j = 0; j < vec_len(params); j++) {
        if (!memcmp("../", p, 3)) {
        if (!memcmp("./", p, 2)) {
        if (!mkstemps(asmfile, 2))
        if (!node->flabel) {
        if (!node->flabel) {
        if (!node->slabel) {
        if (!r) {
        if (!strcmp(k, key)) {
        if (*p == '#') {
        if (*p == '/') {
        if (*p == '/') {
        if (addr) {
        if (avail <= written) {
        if (avail <= written) {
        if (basetype->kind == KIND_STRUCT && next_token(';')) {
        if (next_token('.')) {
        if (next_token('.')) {
        if (p[0] == '\r' && p[1] == '\n') {
        if (p[0] == '\r' && p[1] == '\n') {
        if (p[0] == '\r' || p[0] == '\n') {
        struct { char a:4; char :0; char b:4; };
        struct { char a:4; char b:4; char : 8; };
        struct { char a:5; int b:5; };
        struct { int a:5; int b:5; };
        } else if (is_flotype(v->ty)) {
        } else if (is_flotype(v->ty)) {
        } else if (tok->kind == TIDENT) {
        } else if (ty->isstatic && !isglobal) {
        } else if (val->kind == AST_GVAR) {
        } else {
        } else {
        } else {
        } else {
        } else {
        } else {
        } else {
        } else {
        } else {
        } else {
        } else {
        } else {
        } else {
        } else {
        } else {